import sys
from PIL import Image

# Define los caracteres ASCII que usarás para representar los diferentes niveles de gris
ASCII_CHARS = '@%#*+=-:. '


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def image_to_grayscale(image):
    return image.convert('L')


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]  # Ajusta los caracteres según la intensidad del gris
    return ascii_str


def main(image_path, output_path):
    try:
        # Carga la imagen
        image = Image.open(image_path)

        # Convierte la imagen a escala de grises
        grayscale_image = image_to_grayscale(resize_image(image))

        # Convierte los píxeles de la imagen a caracteres ASCII
        ascii_str = pixels_to_ascii(grayscale_image)

        print(ascii_str)

        # Escribe la salida en un archivo
        with open(output_path, 'w') as file:
            file.write(ascii_str)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Verifica si se proporcionaron los argumentos adecuados
    if len(sys.argv) != 2:
        print("Uso: python ascii_art.py ruta_de_la_imagen ruta_de_salida")
        sys.exit(1)

    # Obtiene la ruta de la imagen y la ruta de salida desde los argumentos de la línea de comandos
    image_path = sys.argv[1]
    output_path = "asciiart/image2.txt"

    # Llama a la función principal con las rutas proporcionadas
    main(image_path, output_path)

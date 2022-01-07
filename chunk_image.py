from PIL import Image

def make_horizontal(image, max_chunk_size=2000):
    # use floor division to get number of chunks
    # use modulus to get size of remainder
    # the remainder counts as an extra chunk.
    # always do it as the last step, even when there are "no chunks" per floor division. in that case, it is the height
    chunks = image.height // max_chunk_size
    remainder = image.height % max_chunk_size

    new_image = Image.new(mode='RGB', size=(image.width * (chunks+1), min(max_chunk_size, image.height)))
    croppings = []
    if chunks or remainder:
        for chunk in range(chunks):
            start = chunk * max_chunk_size
            end = start+max_chunk_size
            cropped = image.crop((0, start, image.width, end))
            if check_cropped(cropped):
                new_image.paste(cropped, box=(image.width * chunk, 0))
                croppings.append(cropped)
        if remainder:
            cropped = image.crop((0, image.height-remainder, image.width, image.height))
            if check_cropped(cropped):
                new_image.paste(cropped, box=(image.width * chunks, 0))
                croppings.append(cropped)

    new_image = new_image.crop((0,0,image.width*len(croppings), new_image.height))
    return new_image

def check_cropped(img):
    """Checks to see if a cropped image has more than one color
    if all one color, returns false"""
    data = img.getdata()
    return not all(data[0] == rgb for rgb in data)

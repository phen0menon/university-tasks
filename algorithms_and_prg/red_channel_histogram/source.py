from PIL import Image, ImageDraw


def hist_draw(hist_name, img_height, hist_data):
    hist = Image.new("RGB", (len(hist_data), img_height), "white")
    draw = ImageDraw.Draw(hist)

    for i in range(len(hist_data)):
        draw.line(((i, img_height), (i, img_height - hist_data[i] / float(max(hist_data)) * img_height)), fill="red")

    hist.save(hist_name)

def main():
    filename = "file.jpg"

    img = Image.open(filename)
    colors = img.getcolors(img.size[0] * img.size[1])
    hist_arr = [0 for i in range(256)]

    for num, color in colors:
        hist_arr[color[0]] += num

    hist_draw("hist1.png", 100, hist_arr)

if __name__ == "__main__":
    main()
files = ["input.png", "slim_sample.png", "steve_sample.png", "slim_2.png"]

from PIL import Image
import os

im = Image.open(files[0]).convert('RGBA')
pixelMap = im.load()

class Colors:
    PINK = '\033[95m' # Pink
    BLUE = '\033[94m' # Blue
    CYAN = '\033[96m' # Cyan
    GREEN = '\033[92m' # Green
    YELLOW = '\033[93m' # Yellow
    RED = '\033[91m' # Red
    RESET = '\033[0m' # No color
    BOLD = '\033[1m' # Bold
    UNDERLINE = '\033[4m' # Underline

if __name__ == '__main__':
    for i, dirs, files in os.walk("input"):
        for file in files:
            filename = file
            file = os.getcwd() + "/input/" + file
            im = Image.open(file).convert('RGBA')
            pixelMap = im.load()

            img = Image.new("RGBA", (64, 64))
            pixelsNew = img.load()

            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    done = False

                    if 16 <= y <= 35:
                        if 47 <= x <= 55:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 45:
                            pixelsNew[x, y] = pixelMap[x, y]
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 46:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                    if 36 <= y <= 47:
                        if 47 <= x <= 55:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 45:
                            pixelsNew[x, y] = pixelMap[x, y]
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 46:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                    if 48 <= y <= 63:
                        if 39 <= x <= 47:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if 55 <= x <= 62:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 37:
                            pixelsNew[x, y] = pixelMap[x, y]
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 38:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 53:
                            pixelsNew[x, y] = pixelMap[x, y]
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 54:
                            pixelsNew[x + 1, y] = pixelMap[x, y]
                            done = True

                        if x == 63:
                            pixelsNew[x, y] = pixelMap[x - 1, y]
                            done = True

                    if not done:
                        pixelsNew[x, y] = pixelMap[x, y]

            im.close()
            img.save("temp.png")
            img.close()

            im2 = Image.open("temp.png").convert('RGBA')
            pixelMap2 = im2.load()

            os.remove("temp.png")

            img2 = Image.new("RGBA", (64, 64))
            pixelsNew2 = img2.load()

            for x in range(img2.size[0]):
                for y in range(img2.size[1]):
                    done = False

                    if 16 <= y <= 19 or 32 <= y <= 35:
                        if x == 50:
                            pixelsNew2[x, y] = pixelMap2[x - 1, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 51:
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                    if 48 <= y <= 51:
                        if x == 42:
                            pixelsNew2[x, y] = pixelMap2[x - 1, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 43:
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 58:
                            pixelsNew2[x, y] = pixelMap2[x - 1, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 59:
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                    if 52 <= y <= 63:
                        if x == 46:
                            pixelsNew2[x, y] = pixelMap2[x, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 47:
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 62:
                            pixelsNew2[x, y] = pixelMap2[x, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 63:
                            pixelsNew2[x, y] = pixelMap2[x - 1, y]
                            done = True

                    if 20 <= y <= 31 or 36 <= y <= 47:
                        if x == 53:
                            pixelsNew2[x, y] = pixelMap2[x - 1, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                        if x == 55:
                            pixelsNew2[x, y] = pixelMap2[x - 1, y]
                            pixelsNew2[x + 1, y] = pixelMap2[x, y]
                            done = True

                    if not done:
                        pixelsNew2[x, y] = pixelMap2[x, y]

            im2.close()

            count = 0
            for cwd, dirs, files in os.walk("output"):
                count = len(files)

            if count > 0:
                img2.save(f"output/output-{count}.png")
            else:
                img2.save(f"output/output.png")

            print(Colors.GREEN + '"' + Colors.CYAN + filename + Colors.GREEN + '" Has been converted and saved as "' + Colors.PINK + f"output-{count + 1}.png" + Colors.GREEN + '"' + Colors.RESET)
            img2.close()

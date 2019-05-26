# 输入图片，在图片上加上数字然后输出
from PIL import Image, ImageFont, ImageDraw

def addcount():
    outputPath = r"D:\\workspace\\pycharm\\show-me-the-code\\show-me-the-code\\chapter01\\images\\";
    fontPath = r"D:\\workspace\\pycharm\\show-me-the-code\\show-me-the-code\\chapter01\\images\\Font\\";
    inputFile = "input.jpg"
    outFile = "output.jpg"

    image = Image.open(outputPath+inputFile, 'r');
    draw = ImageDraw.Draw(image)

    fontSize = int(min(image.size) / 4) ;
    print(fontSize);
    # 增加文字
    fontobj = ImageFont.truetype(font = fontPath + "arial.ttf", size = fontSize, index = 0, encoding = '')
    draw.text((image.size[0] - fontSize, 0), text="11", fill=(255, 0, 0), font=fontobj,
              anchor=None)  # 用draw对象的text()方法添加文字
    image.save(outputPath + outFile)  # 保存图片
    return 0;

if __name__ == '__main__':
    addcount();

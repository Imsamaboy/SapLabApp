#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2 as cv

from handler.type_handler import handle
from handler.split_handler import run_split
from models.page import Page
from utils.draw_utils import draw_x_density
from utils.utils import read_from_pdf


class TeXerApp:
    def __init__(self):
        """
        !singleton class!
        Эксземпляр создаётся при заходе в приложение.
        Происходит подгрузка всех необходимых данных для других модулей.
        """
        pass

    def main(self, path="", pages="406"):
        """
        default - 20
        :param path:
        :param pages: много текста: 406
        :return:
        """
        pages = [Page(simple_image) for simple_image in read_from_pdf(path, pages)]
        for page in pages:
            page.create_image_boxes()
        handle(pages)
        for page in pages:
            # images = []
            # print(len(page.get_image_boxes()))
            print("IMAGEBOXES")
            for image_box in page.get_image_boxes():
                print("ImageBox coords")
                print(image_box.coords)
                # cv.imshow("", image_box.original_image_box)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
            # draw_x_density(image_box)
            # show_images("", images)
            run_split(page.get_image_boxes())
        for page in pages:
            for count, image_box in enumerate(page.get_image_boxes()):
                # print(image_box.type, count + 1)
                # cv.imshow("ImageBox", image_box.original_image_box)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
                if image_box.get_line_boxes():
                    print("LINEBOXES")
                    for line_box in image_box.get_line_boxes():
                        # print(line_box.line_number)
                        # cv.imshow("LineBox", line_box.original_line_image_box)
                        # cv.waitKey(0)
                        # cv.destroyAllWindows()
                        print("LineBox coords")
                        print(line_box.coords)
                        line_box.split_line_box_into_words()
                        # print("Words:")
                        for word_box in line_box.word_boxes:
                            # cv.imshow("word", word_box.original_word_image_box)
                            # cv.waitKey(0)
                            # cv.destroyAllWindows()
                            # draw_x_density(word)
                            print("WordBox coords")
                            print(word_box.coords)
                            # print("Units")
                            word_box.split_word_box_into_units()
                            for unit in word_box.unit_boxes:
                                # print("unit")
                                print("Unit coords")
                                print(unit.coords)
                                # cv.imshow("units", unit.original_unit_image_box)
                                # cv.waitKey(0)
                                # cv.destroyAllWindows()


                else:
                    pass
                    # print("else")


if __name__ == "__main__":
    TeXerApp().main(path="/home/sfelshtyn/Python/SapLabApp/tom3.pdf")

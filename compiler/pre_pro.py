import re


class PrePro:
    @staticmethod
    def filter(file_name):

        try:

            cleaned_source = ""

            with open(file=file_name, mode="r") as f:
                source = f.readlines()

                for l in source:
                    cleaned_source += re.sub(r"hummm.*$", "", l, flags=re.MULTILINE)

            return cleaned_source

        except Exception as error:
            raise TypeError(error)
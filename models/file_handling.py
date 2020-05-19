class FileHandling:
    def __init__(self):
        try:
            self.f = open("sample.txt", 'x')
            self.f.close()
        except Exception as e:
            print(e)

    def addition(self):
        self.f = open("sample.txt", 'a')
        self.f.write("hello world")


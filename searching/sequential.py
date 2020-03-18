class Sequential:
    def search(self, arr, num):
        for x in arr:
            if x == num:
                return True
        return False
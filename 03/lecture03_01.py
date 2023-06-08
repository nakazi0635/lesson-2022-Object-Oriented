import abc

class FizzBuzzBase:

    __DEFAULT_LOOP_TIME = 20

    def __init__(self, max_count=__DEFAULT_LOOP_TIME):
        self.print_fizzbuzz(max_count)

    @abc.abstractmethod
    def __convert(self, input : int) -> str:
        """
        数値をFizzBuzzルールに従って文字列に変換する処理

        Parameters
        ----------
        input : int
            正の整数
        
        Returns
        -------
        result_str : str
            FizzBuzzルールに従って変換した文字列
        """
        # raise NotImplementedError()

    @abc.abstractmethod
    def print_fizzbuzz(self, max_count : int) -> None:
        """
        結果を出力する処理
        max_countには1以上の整数が入力されることを前提としているので例外処理は不要

        Parameters
        ----------
        max_count : int
            1からmax_countまで__convert処理を繰り返す
            __convertから得られた文字列をprintする
        """
        raise NotImplementedError()

class FizzBuzz(FizzBuzzBase):
    def __init__(self, max_count):
        super().__init__(max_count)

    def __convert(self, input : int) -> str:
        result_str = "FizzBuzz" if input%15==0 else "Fizz" if input%3==0 else "Buzz" if input%5==0 else f"{input}"
        return result_str

    def print_fizzbuzz(self, max_count : int) -> None:
        number_list : list[int] = list(range(max_count))
        number_list = list(map(lambda x: x+1, number_list))
        for x in map(self.__convert, number_list):
            print(x)

if __name__ == '__main__':
    FizzBuzz(100)
    # FizzBuzz(1)

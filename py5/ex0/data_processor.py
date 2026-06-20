import typing
import abc


class DataProcessor(abc.ABC):
    @abc.abstractmethod
    def ingest(self, data: any):


    def output(self) -> tuple[int, str]:
        pass

class NumericProcessor(DataProcessor):


class TextProcessor(DataProcessor):


class LogProcessor(DataProcessor):
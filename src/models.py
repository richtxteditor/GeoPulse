import pandas as pd

class DataSource:
    """A base class for all data sources."""
    def __init__(self, name: str, data: pd.DataFrame):
        """Initializes the DataSource.

        Args:
            name: The name of the data source.
            data: The data as a pandas DataFrame.
        """
        self.name = name
        self.data = data

    def get_data(self) -> pd.DataFrame:
        """Returns the data as a pandas DataFrame."""
        return self.data

class Sipri(DataSource):
    """Represents a data source from the Stockholm International Peace Research Institute (SIPRI)."""
    def __init__(self, name: str, data: pd.DataFrame):
        """Initializes the Sipri data source."""
        super().__init__(name, data)

class WorldBank(DataSource):
    """Represents a data source from the World Bank."""
    def __init__(self, name: str, data: pd.DataFrame):
        """Initializes the WorldBank data source."""
        super().__init__(name, data)

class Bloomberg(DataSource):
    """Represents a data source from Bloomberg."""
    def __init__(self, name: str, data: pd.DataFrame):
        """Initializes the Bloomberg data source."""
        super().__init__(name, data)
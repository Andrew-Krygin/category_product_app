import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.loader import load_categories_from_file, read_file
from tests.tests_data.data_for_loader import DATA_FOR_READ_FILE, EXPECTED_RESULT

json_data = json.dumps(DATA_FOR_READ_FILE, indent=4, ensure_ascii=False)


class TestLoader:
    def test_read_file(self) -> None:
        with patch("builtins.open", mock_open(read_data=json_data)) as mock_file:
            with patch("json.load", return_value=DATA_FOR_READ_FILE) as mock_json_load:
                result = read_file("fake/path.json")  # type: ignore
                assert result == DATA_FOR_READ_FILE
                mock_json_load.assert_called_once()
                mock_file.assert_called_once_with("fake/path.json", encoding="utf-8")

    @patch("builtins.open")
    def test_read_file_exception_file_not_found(self, mock_open_file: MagicMock) -> None:
        mock_open_file.side_effect = FileNotFoundError("message")

        with pytest.raises(FileNotFoundError):
            read_file("invalid/path.json")  # type: ignore

    @patch("builtins.open", new_callable=mock_open, read_data="not json")
    def test_read_file_json_decode_error(self, mock_open_file: MagicMock) -> None:
        with pytest.raises(json.JSONDecodeError):
            read_file("invalid.json")  # type: ignore
            mock_open_file.assert_called_once()

    def test_load_categories_from_file(self) -> None:
        with patch("src.loader.read_file") as mock_read:
            mock_read.return_value = DATA_FOR_READ_FILE
            result = load_categories_from_file()
            assert result == EXPECTED_RESULT

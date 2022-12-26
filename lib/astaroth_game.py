from pyrogram.types import Message
import re

class AstarothGame():
  def __init__(self):
    self.played_numbers: list[str] = []
    self.unplayed_numbers: list[str] = []

  def set_played_numbers(self, message: Message):
    matched_numbers: list[str] = re.findall(r"\d+", message.text)
    min_number = int(matched_numbers[0])
    max_number = int(matched_numbers[1])
    played_numbers =  ["-" for x in range(min_number, max_number + 1)]
    self.played_numbers = played_numbers

  def set_unplayed_numbers(self, message: Message):
    matched_numbers: list[str] = re.findall(r"\d+", message.text)
    min_number = int(matched_numbers[0])
    max_number = int(matched_numbers[1])
    unplayed_numbers = list(range(min_number, max_number + 1))
    self.unplayed_numbers = list(map(str, unplayed_numbers))

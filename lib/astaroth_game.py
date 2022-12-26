from pyrogram.types import Message
import re

class AstarothGame():
  def __init__(self):
    self.played_numbers: list[str] = []
    self.unplayed_numbers: list[str] = []
    self.init_numbers_played = False

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

  def update_init_numbers(self, message: Message):
    if self.init_numbers_played: return
    self.init_numbers_played = True
    matched_numbers: list[str] = re.findall(r"\d+", message.text)
    next_number_index = 1

    while True:
      try:
        played_number = matched_numbers[next_number_index]
        self.played_numbers[int(played_number) - 1] = played_number
        self.unplayed_numbers[int(played_number) - 1] = "-"
        next_number_index += 3
      except: break

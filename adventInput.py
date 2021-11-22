from pathlib import Path

def GetInput(day):
  formattedDay = day
  if day < 10:
    formattedDay = f"0{day}"
  data_folder = Path(f"Day{formattedDay}/")
  file_path = data_folder / f"Day{formattedDay}Input.txt"
  input = open(file_path).readlines()
  input = [s.rstrip() for s in input]
  return input
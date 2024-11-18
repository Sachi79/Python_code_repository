symbol_prefix_numeric_mapping_dict = {
  "d": -1,
  "c": -2,
  "m": -3,
  "µ": -6,
  "n": -9,
  "p": -12,
  "f": -15,
  "a": -18,
  "da": 1,
  "h": 2,
  "k": 3,
  "M": 6,
  "G": 9,
  "T": 12,
  "P": 15,
  "E": 18
}
symbol_numeric_prefix_mapping_dict = {v: k for k, v in symbol_prefix_numeric_mapping_dict.items()}

print(symbol_numeric_prefix_mapping_dict)

print(symbol_prefix_numeric_mapping_dict)

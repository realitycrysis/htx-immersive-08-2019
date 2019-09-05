def word_count(string):
  my_string = string.lower().split()
  my_dict = {}
  for item in my_string:
    my_dict[item] = item.count(item)
  print(my_dict)

word_count("I do not want green eggs and ham, I do not like this Sam I am!")

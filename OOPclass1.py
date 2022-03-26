from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["pokemon", "Type"]
table.add_row(["pikachu","Electric"])
table.add_row(["squrite","Water"])
table.add_row(["charmander","fire"])
table.add_row(["mangoe","wind"])
print(table)

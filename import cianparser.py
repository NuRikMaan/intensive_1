import cianparser

moscow_parser = cianparser.CianParser(location="Красногорск")
data = moscow_parser.get_flats(deal_type="sale", rooms=(3, 4), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1000})

print(data[0])
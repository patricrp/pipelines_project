from argparse import ArgumentParser
from src.functions import totalViews

def main():
    pais, year = parser() 
    print(pais, year)
    print(totalViews(pais, year))
    #viewsPerYear(args.pais)
    #createPDF

def parser():
    parser = ArgumentParser(description='Filter the DataFrame by country')
    parser.add_argument('pais', type=str, help='the country you want to filter by')
    parser.add_argument('year', type=int, help='the year of publicacion of travel videos')
    args=parser.parse_args()
    pais = args.pais
    year = args.year
    return pais, year



if __name__ == "__main__":
    main()

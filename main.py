from argparse import ArgumentParser
from src.functions import totalViews

def main():
    pass 

'''def checkPais(pais):
    if pais in countries:
        return pais
    else:
        raise argparse.ArgumentTypeError('')

def checkYear(year):
    if 2007<=int(year)<=2019:
        return int(year)
    else:
        raise argparse.ArgumentTypeError('')'''

def parser():
    parser = ArgumentParser(description='Filter the DataFrame by country')
    parser.add_argument('pais', type=str, nargs = 1, help='the country you want to filter by')
    parser.add_argument('year', type=int, help='the year of publicacion of travel videos')
    return parser.parse_args()



if __name__ == "__main__":
    args=parser()
    totalViews(args.pais, args.year)
    viewsPerYear(args.pais)
    #createPDF

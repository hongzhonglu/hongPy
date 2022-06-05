#!/usr/bin/env python
# pathway_genes.py
# adapted from https://gist.github.com/slowkow/a2327b868f4e927ac4fb
# Feiran Li 2020.02.23

import urllib
from bs4 import BeautifulSoup as bs
import sys

import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd

def main():
    args = sys.argv
    if len(args) != 2:
        print
        'Usage: ./pathway_genes.py PATHWAY'
        sys.exit(1)

    #pathway_id = str(args[1])
     pathway_id = 'map04068'

    orthology_ids = get_orthology_ids(pathway_id)

    print
    'Found {} orthology ids for pathway "{}"' \
        .format(len(orthology_ids), pathway_id)

    if not orthology_ids:
        sys.exit(1)

    for orthology_id in orthology_ids:
        gene_ids = get_gene_ids(orthology_id)

        print
        'Writing {} FASTA gene sequences to "{}.fa"' \
            .format(len(gene_ids), orthology_id)

        with open(orthology_id + '.fa', 'w') as out:
            for i, gene_id in enumerate(gene_ids, 1):
                sys.stdout.write('.')
                if not i % 5:
                    sys.stdout.write(' ')
                if not i % 50:
                    sys.stdout.write('\n')
                sys.stdout.flush()

                fasta = get_fasta(gene_id)
                out.write(fasta)

        print


def get_ids(url):


    url = "https://www.genome.jp/dbget-bin/get_linkdb?-t+uniprot+ko:K00039"
    response = urllib.urlopen(url)
    html = response.read()
    b = bs(html)
    links = b.find_all('pre')
    valid_link = lambda x: 'www_bget' in x.get('href')
    links = filter(valid_link, links)
    return [link.text for link in links]


def get_orthology_ids(pathway_id):
    URL = 'http://www.genome.jp'
    FUN = '/dbget-bin/get_linkdb?-t+orthology+path:'
    return get_ids(URL + FUN + pathway_id)


def get_gene_ids(orthology_id):
    URL = 'http://www.genome.jp'
    FUN = '/dbget-bin/get_linkdb?-t+genes+ko:'
    return get_ids(URL + FUN + orthology_id)


def get_fasta(gene_id):
    URL = 'http://www.genome.jp'
    FUN = '/dbget-bin/www_bget?-f+-n+n+'
    response = urllib2.urlopen(URL + FUN + gene_id)
    html = bs(response.read())
    return html.pre.text


if __name__ == '__main__':
    main()
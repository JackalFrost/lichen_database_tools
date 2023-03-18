# lichen_database_tools
This is a repository of the code and files used for Kerr &amp; Leavitt, 2023.

The files are as follows:
1. Lichen_Data_Parser.py - A Python script used to analyze identification rates for the regional, UNITE at 98%, and UNITE at 98.5% database instances.
2. family_data.txt - A tab-separated file containing numbers of identifications for the three database instances for taxonomic family, based on values found through Lichen_Data_Parser.py
3. full_data_for_python.txt - A tab-separated file containing the OTUs from the geographic sampling sites, with BLAST Percent ID for UNITE, family/genus/species according to the regional database, whether the taxonomy is in the regional database, and counts of sequences found at the various sampling sites.
4. site_id_data.txt - A tab-separated file containing numbers of identifications for the three database instances for geographical sampling site, based on values found through Lichen_Data_Parser.py
5. supplementary_code_barcode_databases.Rmd - An R Markdown document containing code used for running statistical analyses and creating figures.
6. total_data.txt - A tab-separated file containing numbers of total identifications for the three database instances, based on values found through Lichen_Data_Parser.py

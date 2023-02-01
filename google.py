from bing_image_downloader.downloader import download

query_string = '엑소 백현'

download(query_string, limit=2,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
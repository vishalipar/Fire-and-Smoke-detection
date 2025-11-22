from bing_image_downloader import downloader

keywords = [
    'forest fire',
    'wildfire flames',
    'forest fire smoke',
    'bushfire',
    'wildfire aerial view',
    'forest smoke',
    'forest fire drone view',
    'grass fire',
    'mountain fire',
    'forest burning'
]

for k in keywords:
    downloader.download(
        k,
        limit=50,
        output_dir='dataset images',
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )
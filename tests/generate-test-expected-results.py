import json
import os

import imagemounter

from pprint import pprint

images = [
    # from the internet!
    "dftt_images/10-ntfs-disk.dd",
    "dftt_images/11-carve-fat.dd",
    "dftt_images/12-carve-ext2.dd",
    "dftt_images/7-ntfs-undel.dd",
    "dftt_images/8-jpeg-search.dd",
    "dftt_images/9-fat-label.dd",
    "dftt_images/daylight.dd",
    "dftt_images/ext-part-test-2.dd",
    "dftt_images/ntfs-img-kw-1.dd",
    "digitalcorpora/lone_wolf/LoneWolf.E01",
    "digitalcorpora/m57-jean/nps-2008-jean.E01",
    "digitalcorpora/m57-patents/charlie-2009-12-11.E01",
    "digitalcorpora/m57-patents/charlie-work-usb-2009-12-11.E01",
    "digitalcorpora/m57-patents/jo-2009-12-11-001.E01",
    "digitalcorpora/m57-patents/jo-favorites-usb-2009-12-11.E01",
    "digitalcorpora/m57-patents/pat-2009-12-11.E01",
    "digitalcorpora/m57-patents/terry-2009-12-11-001.E01",
    "digitalcorpora/m57-patents/terry-work-usb-2009-12-11.E01",
    "digitalcorpora/national_gallery/tracy-home-2012-07-16-final.E01",
    # broken for unknown reasons
    # 'dftt_images/6-fat-undel.dd',
    # 'dftt_images/ext3-img-kw-1.dd',
    # 'dftt_images/fat-img-kw.dd',
    # 'digitalcorpora/m57-patents/jo-work-usb-2009-12-11.E01',
    # 'digitalcorpora/national_gallery/tracy-external-2012-07-16-final.E01',
    # internally available
    "WinXP2.E01",
    "xp-tdungan/xp-tdungan-c-drive.E01",
]

imgs = []

os.chdir("test_images")

for image_path in images:

    print(f"################### {image_path} ##########################")
    image_parser = imagemounter.ImageParser([image_path])
    disk = image_parser.disks[0]

    img = {"name": disk._name, "imagepath": disk.paths[0], "volumes": []}
    mountable = False
    mountable_checked = False

    for volume in image_parser.init():
        # img['mountpoint'] = disk.mountpoint

        if not mountable_checked and volume.mountpoint not in [None, ""]:
            mountable = True
            mountable_checked = True

        v = {
            "fsdescription": volume.info.get("fsdescription"),
            "label": volume.info.get("label"),
            "size": volume.size,
            "offset": volume.offset,
            "index": int(volume.index),
            "fstype": volume.fstype,
            # 'mountpoint': volume.mountpoint
        }

        img["volumes"].append(v)

    imgs.append(
        {
            "expected_json_response": img,
            "assertions": {
                "disk_mountpoint": bool(disk.mountpoint),
                "num_volumes": len(img["volumes"]),
                "mountable": mountable,
            },
        }
    )

    image_parser.clean()


os.chdir("..")

with open("expected-test-results.json", "w") as fil:
    json.dump(imgs, fil, sort_keys=True, indent=4)

print(
    "####################################################################################"
)
print(
    "##################### ALL DONE! HOORAY!! ###########################################"
)
print(
    "####################################################################################"
)

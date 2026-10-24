"""stations/ 폴더의 이미지를 스캔해서 stations.js 를 다시 만든다.

파일 이름 규칙: 역이름_번호.확장자   예) 사가정_1.webp, 사가정_2.png
(역 이름은 지도에 표시되는 이름과 같아야 함: '역' 글자 없이)
실행: python build_stations.py
"""
import json, os, re

EXT = ('.webp', '.png', '.jpg', '.jpeg')
result = {}
for fn in sorted(os.listdir('stations')):
    m = re.fullmatch(r'(.+)_(\d+)(\.[A-Za-z]+)', fn)
    if not m or m.group(3).lower() not in EXT:
        continue
    name = m.group(1)
    result.setdefault(name, []).append({'file': 'stations/' + fn, 'alt': name + '역 안내도'})

with open('stations.js', 'w', encoding='utf-8') as f:
    f.write('window.STATION_MAPS=' + json.dumps(result, ensure_ascii=False) + ';')
print(len(result), '개 역,', sum(len(v) for v in result.values()), '장')

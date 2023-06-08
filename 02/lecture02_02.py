#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    root = ET.Element('book')
    article = ET.SubElement(root, 'article', attrib = {'title': '卒業論文'})
    # 頭の体操
    # persons = list(map(lambda i: ET.SubElement(human, 'person', attrib={'id': str(i)}), range(10)))
    chapters = []
    article_name = ['はじめに','基礎理論','実験方法','結果と考察','まとめ','参考文献']
    article_page = ['2','8','6','2','1','2']
    for i in range(6):
        chapter = ET.SubElement(article, 'chapter')
        chapter.attrib['id'] = str(i+1) # cast i from int to str
        chapter.attrib['name'] = str(article_name[i])
        chapter.attrib['pages'] = str(article_page[i])
        chapters.append(chapter)
    
    novel = ET.SubElement(root, 'novel')
    novel_name = ['1日のはじまり','朝食','仕事','帰宅後','新しい朝']
    novel_page = ['2','8','6','2','1']
    for i in range(5):
        chapter = ET.SubElement(novel, 'chapter')
        chapter.attrib['id'] = str(i+1)
        chapter.attrib['name'] = str(novel_name[i])
        chapter.attrib['pages'] = str(novel_page[i])
        chapters.append(chapter)


    # write readable xml (have your attention to 'wb')
    with open('lecture02_02_data.xml', 'wb') as f:
        import xml.dom.minidom as md
        f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))


if __name__ == '__main__':
    lecture02_02()
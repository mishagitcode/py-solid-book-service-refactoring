import json
import xml.etree.ElementTree as ElTree


class Serializer:
    def serialize(self, book) -> None:
        raise NotImplementedError


class JsonSerializer(Serializer):
    def serialize(self, book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def get_serializer(serialize_type: str) -> Serializer:
        if serialize_type == "json":
            return JsonSerializer()
        elif serialize_type == "xml":
            return XmlSerializer()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

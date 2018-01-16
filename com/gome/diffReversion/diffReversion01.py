import xml.dom.minidom

path = "2018-01-15-05-15-01.xml"

dom = xml.dom.minidom.parse(path)

projects = dom.getElementsByTagName("project")

print(len(projects))

for project in projects:
    nameValue = project.getAttribute("name")
    revisionValue = project.getAttribute("revision")
    upstreamValue = project.getAttribute("name")
    print("name={} reversion={} upstream={}".format(nameValue, revisionValue, upstreamValue))
print(type(projects))
# 得到文档元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

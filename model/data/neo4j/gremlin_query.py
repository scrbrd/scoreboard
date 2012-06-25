""" Module: Gremlin Query

Generate reusable components of Gremlin queries and build full scripts
for issuing calls to a Neo4j graph database.

"""


def and_then():
    #return GREMLIN_QUERY.AND_THEN
    return "."


def get_graph():
    #return GREMLIN_QUERY.GRAPH
    return "g"


def get_it():
    return "it"


def as_pipe():
    return "_()"


def add_vertex(vertex):
    return "addVertex({0})".format(vertex)


def add_edge(from_id, to_id, type, properties):
    return "addEdge({0}, {1}, {2}, {3})".format(
            get_vertex(from_id),
            get_vertex(to_id),
            type,
            properties)


def get_vertex(id):
    return "v({0})".format(id)


def get_vertex_out_edges(vertex):
    return "{0}{1}{2}".format(vertex, and_then(), get_out_edges())


def get_out_edges(types=[]):
    return "outE({0})".format(all(types))


def get_out_vertices(types=[]):
    return "out({0})".format(all(types))


def get_index(index):
    return "idx({0})".format(in_quotes(index))


def get_indexed_vertices_collection(key, value):
    return "get({0}, {1})".format(key, value)


def get_vertex_and_out_edges(id):
    return "{0}{1}{2}{3}{4}".format(
            get_graph(),
            and_then(),
            get_vertex(id),
            and_then(),
            transform_vertex_and_out_edges(get_it()))


# TODO: finish this function!
#def get_indexed_vertices_and_out_edges(
#        key,
#        value,
#        )

def get_adjacent_vertices_and_out_edges(
        id,
        edge_types,
        vertex_key,
        vertex_types):
    return "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(
            get_graph(),
            and_then(),
            get_vertex(id),
            and_then(),
            get_out_vertices(edge_types),
            and_then(),
            dedup(),
            maybe_filter_matches(get_it(), vertex_key, vertex_types),
            transform_vertex_and_out_edges(get_it()))


def get_depth1_path(id, edge_types, vertex_key, vertex_types):
    d0 = "d0"
    d1 = "d1"

    start = "{0} = {1}; ".format(d0, get_vertex_and_out_edges(id))
    adjacent = "{0} = {1}; ".format(d1, get_adjacent_vertices_and_out_edges(
        id,
        edge_types,
        vertex_key,
        vertex_types))
    path = collection(["d0", "d1"])

    return "{0}{1}{2}".format(start, adjacent, path)


def transform(closure):
    return "transform{{{0}}}".format(closure)


def transform_vertex_and_out_edges(vertex):
    return transform(collection([vertex, get_vertex_out_edges(vertex)]))


def filter(closure):
    return "filter{{{0}}}".format(closure)


def maybe_filter_matches(vertex, key, values):
    return filter_matches(vertex, key, values) if values else ""


def filter_matches(vertex, key, values):
    return filter("{0}{1}{2}{3}{4}{5}{6}".format(
        vertex,
        and_then(),
        key,
        and_then(),
        matches(values)))


def matches(values):
    return "matches({0})".format(any(values))


def pattern(values, delimiter):
    return "{0}".format(in_quotes(delimiter.join(values)))


def in_braces(string):
    return "{{{0}}}".format(string)


def in_quotes(string):
    return "\"{0}\"".format(string)


def any(values):
    return pattern(values, " | ")


def all(values):
    return pattern(values, ", ")


def dedup():
    return "dedup()"


def has_property(key, value):
    return "has({0}, {1})".format(key, value)


def collection(list):
    return "[{0}]".format(all(list))

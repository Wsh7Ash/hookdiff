from hookdiff.diff import diff, breaking, flatten
def test_flatten():
    assert flatten({'a': {'b': 1}}) == {'a.b': 1}
def test_added_removed_changed():
    old = {'x': 1, 'gone': True}
    new = {'x': 2, 'fresh': 'hi'}
    ch = diff(old, new)
    kinds = {c['path']: c['change'] for c in ch}
    assert kinds == {'gone': 'removed', 'fresh': 'added', 'x': 'changed'}
def test_breaking_filters_added():
    ch = diff({'a': 1, 'c': 5}, {'b': 2, 'c': 6})
    assert sorted(c['change'] for c in breaking(ch)) == ['changed', 'removed']
def test_list_index_paths():
    ch = diff({'items': [1]}, {'items': [1, 2]})
    assert ch[0]['path'] == 'items[1]'
    assert ch[0]['change'] == 'added'

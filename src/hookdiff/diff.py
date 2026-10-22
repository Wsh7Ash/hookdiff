def flatten(obj, prefix=''):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.update(flatten(v, f'{prefix}.{k}' if prefix else k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.update(flatten(v, f'{prefix}[{i}]'))
    else:
        out[prefix] = obj
    return out

def diff(old, new):
    a = flatten(old)
    b = flatten(new)
    changes = []
    for path in sorted(set(a) | set(b)):
        if path not in a:
            changes.append({'path': path, 'change': 'added', 'new': b[path]})
        elif path not in b:
            changes.append({'path': path, 'change': 'removed', 'old': a[path]})
        elif a[path] != b[path]:
            changes.append({'path': path, 'change': 'changed', 'old': a[path], 'new': b[path]})
    return changes

def breaking(changes):
    return [c for c in changes if c['change'] in ('removed', 'changed')]

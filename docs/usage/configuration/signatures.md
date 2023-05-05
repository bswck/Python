# Signatures options

## `annotations_path`

- **:octicons-package-24: Type [`str`][] :material-equal: `"brief"`{ title="default value" }**
- **:octicons-project-template-24: Template :material-null:** (N/A)

The verbosity for annotations path.

Possible values:

- `brief` (recommended): render only the last component of each type path, not their full paths.
    For example, it will render `Sequence[Path]` and not `typing.Sequence[pathlib.Path]`.
    Brief annotations will cross-reference the right object anyway,
    and show the full path in a tooltip when hovering them.
- `source`: render annotations as written in the source. For example if you imported `typing` as `t`,
    it will render `typing.Sequence` as `t.Sequence`. Each part will cross-reference the relevant object:
    `t` will link to the `typing` module and `Sequence` will link to the `Sequence` type.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          annotations_path: brief
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      annotations_path: source
```

```python
import markdown
import markupsafe

def convert(text: str, md: markdown.Markdown) -> markupsafe.Markup:
    """Convert text to Markdown.

    Parameters:
        text: The text to convert.
        md: A Markdown instance.
    
    Returns:
        Converted markup.
    """
    return Markup(md.convert(text))
```

/// admonition | Preview
    type: preview

//// tab | Brief annotations
<h2><code>convert(text, md)</code></h2>
<p>Convert text to Markdown.</p>
<p><b>Parameters:</b></p>

**Type**   | **Description**          | **Default**
---------- | ------------------------ | -----------
[`str`][]  | The text to convert.     | *required*
[`Markdown`](#ref-to-markdown){ .external title="markdown.Markdown" } | A Markdown instance. | *required*

<p><b>Returns:</b></p>

**Type**   | **Name**    | **Description**
---------- | ----------- | ---------------
[`Markup`](#ref-to-markup){ .external title="markupsafe.Markup" } | `text` | Converted markup.
////

//// tab | Source annotations
<h2><code>convert(text, md)</code></h2>
<p>Convert text to Markdown.</p>
<p><b>Parameters:</b></p>

**Type**   | **Description**          | **Default**
---------- | ------------------------ | -----------
[`str`][]  | The text to convert.     | *required*
<code><a class="external" href="#ref-to-markdown">markdown</a>.<a class="external" href="#ref-to-Markdown" title="markdown.Markdown">Markdown</a></code> | A Markdown instance. | *required*

<p><b>Returns:</b></p>

**Type**   | **Name**    | **Description**
---------- | ----------- | ---------------
<code><a class="external" href="#ref-to-markupsafe">markupsafe</a>.<a class="external" href="#ref-to-Markup" title="markupsafe.Markup">Markup</a></code> | `text` | Converted markup.
////
///

## `line_length`

- **:octicons-package-24: Type [`int`][] :material-equal: `60`{ title="default value" }**
- **:octicons-project-template-24: Template :material-null:** (N/A)

Maximum line length when formatting code/signatures.

When separating signatures from headings with the [`separate_signature`][] option,
the Python handler will try to format the signatures using [Black] and
the specified line length.

If Black is not installed, the handler issues an INFO log once.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          separate_signature: true
          line_length: 60
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      separate_signature: true
      line_length: 80
```

/// admonition | Preview
    type: preview

//// tab | Line length 60
<h2>long_function_name</h2>
<pre><code>long_function_name(
    long_parameter_1="hello",
    long_parameter_2="world",
)</code></pre>
////

//// tab | Line length 80
<h2>long_function_name</h2>
<pre><code>long_function_name(long_parameter_1="hello", long_parameter_2="world")</code></pre>
////
///

## `show_signature`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
- **:octicons-project-template-24: Template :material-null:** (N/A)

Show methods and functions signatures.

Without it, just the function/method name is rendered.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_signature: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_signature: false
```

/// admonition | Preview
    type: preview

//// tab | With signature
<h2><code>function(param1, param2=None)</code></h2>
<p>Function docstring.</p>
////

//// tab | Without signature
<h2><code>function</code></h2>
<p>Function docstring.</p>
////
///

## `show_signature_annotations`
bool 	

Show the type annotations in methods and functions signatures. Default: False.

## `separate_signature`
bool 	

Whether to put the whole signature in a code block below the heading. If Black is installed, the signature is also formatted using it. Default: False.
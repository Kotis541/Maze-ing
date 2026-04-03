<i>This project has been created as part
of the 42 curriculum by vokotera and pzavada<i>

<h1>Description</h1>
A-maze-ing is a Python maze generator and visualizer. The program reads a configuration file, generates a valid maze with embed 42 pattern in the center. After that it writes the result into the output file using hexadecimal wall encoding.

<h1> Instructions </h1>

<h3>Installation</h3>
<pre>make install </pre>
This install all project dependencies via pip

<h3>Running program</h3>
<pre>make run</pre>
or
<pre>./a-maze-ing.py config.txt</pre>

**Debug mode**
<pre>make debug</pre>

<h3>Linting</h3>
<pre>make lint</pre>

<h3>Cleanup</h3>
<pre>make clean</pre>

---

**Configuration File**

The configuration file uses `KEY=VALUE` pairs (one per line). Lines starting with `#` are comments and are ignored.

| Key           | Description                          | Example                  
|---------------|--------------------------------------|--------------------------
| `WIDTH`       | Maze width (number of cells)         | `WIDTH=20`               |
| `HEIGHT`      | Maze height (number of cells)        | `HEIGHT=15`              |
| `ENTRY`       | Entry cell coordinates (x,y)         | `ENTRY=0,0`              |
| `EXIT`        | Exit cell coordinates (x,y)          | `EXIT=19,14`             |
| `OUTPUT_FILE` | Path to the output file              | `OUTPUT_FILE=maze.txt`   |
| `PERFECT`     | Generate a perfect maze (True/False) | `PERFECT=True`           |
| `SEED`        | Random seed for reproducibility      | `SEED=42`                |


**Example `config.txt`:**
```ini
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```


<h1>Resources</h1>

 - [Youtube - Maze algorithm](https://www.youtube.com/watch?is=g33h4t98knfFA5SB&v=jZQ31-4_8KM)

### AI usage
- AI tools were used during the development of this project to gain a deeper understanding of the core concepts and to assist with coding and debugging. No code was blindly copy-pasted without a full comprehension of its functionality
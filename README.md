# 🎉 FancyPy: Fancify Your Titles into Block Comments

FancyPy is a simple Python script that turns your titles or headers into fancy block comments, suitable for a variety of programming languages like Python, C, C++, Java, MATLAB, and LaTeX. ✨

## 🔧 How to Run the Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alipoosti/fancyPy
   cd fancyPy
   ```

2. **Run the script**:
   ```bash
   python fancyPy.py "Your Title Here" [options]
   ```

### 📋 Arguments

- `title string`: The title you want to "fancify."
- `--style STYLE`, `-S STYLE`: Choose the comment block style (`Python`, `C`, `C++`, `Java`, `MATLAB`, `LaTeX`). Default is `Python`.
- `--length LENGTH`, `-L LENGTH`: Set the block length. Default is 40.
- `--output`, `-O`, `-o`: Optionally save the output to a `.txt` file.
- `--filename FILENAME`, `-F FILENAME`: If `output` is specified, set the filename for the output. Default is `fancyPy_output`.

## 💻 Example Usage

```bash
python fancyPy.py "My Fancy Title" --style Python --length 50 --output
```

This will output a fancy Python-style comment block and save it to `fancyPy_output.txt`.

The fancy header output then looks like:

    ```txt
    ##################################################
    ################# My Fancy Title #################
    ##################################################

    Comment Style: Python
    ```

For other styles, the output looks like:

- MATLAB/LaTeX

    ```txt
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%% My Fancy Title %%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    Comment Style: MATLAB/LaTeX
    ```

- C/C++/Java 

    ```txt
    /*
    --------------------------------------------------
                    My Fancy Title                  
    --------------------------------------------------
    */

    Comment Style: C/C++/Java
    ```

## 📝 How It Works

1. **Input Title**: The script takes your title(s) and turns them into a block comment.
2. **Choose Style**: You can choose the style of the comment block, such as Python, C, Java, etc.
3. **Adjust Block Length**: You can adjust the block length to make sure it fits your title properly.
4. **Output to File**: You can save the result to a `.txt` file.

## 🚀 Add to `.bashrc` or `.zshrc` for Quick Access

To easily run the script from any directory, add an alias to your `.bashrc` or `.zshrc`:

1. Open your `.bashrc` or `.zshrc` file:
   ```bash
   nano ~/.bashrc  # or ~/.zshrc
   ```

2. Add the following line to create an alias for the script:
   ```bash
   alias fancify="python /path/to/fancyPy.py"
   ```

3. Reload the shell configuration:
   ```bash
   source ~/.bashrc  # or ~/.zshrc
   ```

4. Now you can simply run:
   ```bash
   fancify "My Fancy Title"
   ```

## ⚙️ Requirements

- Python 3.x

---

Enjoy making your titles extra fancy! 😎🎨

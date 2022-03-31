import pandas as pd
import seaborn as sns

# Set default plot style
sns.set_style('whitegrid')
sns.set_palette('colorblind')

def save_figure(figure, filename, x=None, y=None):
    '''Save a FIGURE to FILENAME with size of X, Y inches.'''
    fig = figure.get_figure()
    plt.tight_layout()
    if x is not None:
        fig.set(figwidth = x)
    if y is not None:
        fig.set(figheight = y)
    fig.savefig(filename, dpi=600)
    plt.close(fig)

def make_figure(data, x, y, hue, condition, base):
    '''Make a comparison figure from DATA (appropriately grouped and
summarized), of size X, Y inches.  Filenames are form BASE-true.png,
BASE-false.png, where true and false refer to the CONDITION, i.e., a
series describing included row-keys.
    '''
    data_true = data[condition]
    data_false = data[condition.apply(lambda x:not x)]
    save_figure(sns.boxplot(x=x, y=y, hue=hue, data=data_true), f"{base}-true.png")
    save_figure(sns.boxplot(x=x, y=y, hue=hue, data=data_false), f"{base}-false.png")

def save_table(df, filename, decimals=2, colsep=False, **kwargs):
    global colsepname
    if not colsep is False:
        colsepname = colsepname + 'A'

    pd.options.display.float_format = ('{:,.' + str(decimals) + 'f}').format

    with pd.option_context("max_colwidth", 1000):
        tab1 = df.to_latex(**kwargs)
    # print(tab1)
    with open(filename,'w',encoding='utf-8') as f:
        f.write('% DO NOT EDIT\n')
        f.write('% this file was automatically generated\n')
        if not colsep is False:
            f.write('\\newcommand{\\oldtabcolsep' + colsepname + '}{\\tabcolsep}\n')
            f.write('\\renewcommand{\\tabcolsep}{' + colsep + '}\n')
        f.write(tab1)
        if not colsep is False:
            f.write('\\renewcommand{\\tabcolsep}{\\oldtabcolsep' + colsepname +'}\n')

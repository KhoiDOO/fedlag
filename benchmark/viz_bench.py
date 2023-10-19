import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")


if __name__ == "__main__":
    results_plot_data = os.getcwd() + "/results_plot/plot_data.csv"
    res_df = pd.read_csv(results_plot_data)
    
    bm_plot_dir = results_plot_data = os.getcwd() + "/results_plot/benchmark_plot"
    if not os.path.exists(bm_plot_dir):
        os.mkdir(bm_plot_dir)
    
    ds_lst = res_df['ds'].unique().tolist()
    
    for _ds in ds_lst:
        _ds_df = res_df[res_df['ds'] == _ds]
        
        ds_plot_dir = bm_plot_dir + f"/{_ds}"
        if not os.path.exists(ds_plot_dir):
            os.mkdir(ds_plot_dir)
        
        ucnt_lst = _ds_df["user"].unique().tolist()
        
        for _unct in ucnt_lst:
            _unct_df = _ds_df[_ds_df['user'] == _unct]
            
            us_plot_dir = ds_plot_dir + f"/{_unct}"
            if not os.path.exists(us_plot_dir):
                os.mkdir(us_plot_dir)
            
            for metrics in ["test_acc", "test_auc_std", "train_loss", "test_acc_std", "test_auc"]:
                sns.lineplot(x="rounds", y=metrics, hue="algo", data=_unct_df)
                
                plt.savefig(us_plot_dir + f"/{metrics}.pdf", dpi=300, format='pdf')
                
                plt.close()
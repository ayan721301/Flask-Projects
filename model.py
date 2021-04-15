import numpy as np
import pandas as pd 

def model(name):
        data = pd.read_csv(r'data.csv')
        name1 = name.split()
        num = len(name1)
        df1 = data[name1]
        stock = name1
        mean_returns = data[name1].mean()
        cov_matrix = data[name1].cov()
        num_iterations = 10000
        simulation_res = np.zeros((4 + num - 1,num_iterations))
        for i in range(num_iterations):
                weights = np.array(np.random.random(num))
                weights /= np.sum(weights)
                portfolio_return = np.sum(mean_returns * weights)
                portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights)))
                simulation_res[0,i] = portfolio_return
                simulation_res[1,i] = portfolio_std_dev
                simulation_res[2,i] = simulation_res[0,i] / simulation_res[1,i]
                for j in range(len(weights)):
                        simulation_res[j+3,i] = weights[j]
        if num == 2: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1]])
        elif num == 3: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2]])
        elif num == 4: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3]])
        elif num == 5: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4]])
        elif num == 6: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4],stock[5]])
        elif num == 7: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4],stock[5],stock[6]])
        elif num == 8: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4],stock[5],stock[6],stock[7]])
        elif num == 9: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4],stock[5],stock[6],stock[7],stock[8]])
        elif num == 10: 
                sim_frame = pd.DataFrame(simulation_res.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4],stock[5],stock[6],stock[7],stock[8],stock[9]])
        max_sharpe = round(sim_frame.iloc[sim_frame['sharpe'].idxmax()],4)
        min_std = round(sim_frame.iloc[sim_frame['stdev'].idxmin()],4)
        a =  (max_sharpe*100).to_string()
        b = (min_std*100).to_string()
        return a, b

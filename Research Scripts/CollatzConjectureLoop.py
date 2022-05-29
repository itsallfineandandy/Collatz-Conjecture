import pandas as pd
import os

df = pd.DataFrame(columns=['I', 'Interations', 'Max'])

if (os.path.isfile('/Users/andrewhaley/Github Repos/Research Projects/Collatz-Conjecture/Data/LatestProgressLoop.csv')):
  df = pd.read_csv('/Users/andrewhaley/Github Repos/Research Projects/Collatz-Conjecture/Data/LatestProgressLoop.csv')

i = df['I'].max()
if(pd.isnull(i)):
  i = 1
while(i < 100000000001):
  test = i
  interations = 0
  MaxNum = i
  while(test != 1):
    if test % 2 == 0:
      test = test/2
    else:
      test = test*3+1
    interations = interations+1
    MaxNum = max(MaxNum,test)
  df = pd.concat([df, pd.DataFrame.from_records([{'I': i, 'Interations': interations, 'Max': MaxNum}])])
  if i % 10000 == 0:
    df.to_csv('/Users/andrewhaley/Github Repos/Research Projects/Collatz-Conjecture/Data/LatestProgressLoop.csv', index=False)
  print("I = ", str(i)," Interations = ",str(interations)," Max = ",str(MaxNum))
  i = i+1

print(df)

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB, GaussianNB, MultinomialNB, ComplementNB, BernoulliNB

iris = sns.load_dataset('iris')
iris.head()
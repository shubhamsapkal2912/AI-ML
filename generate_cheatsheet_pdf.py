from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_cheatsheet_pdf(filename="ML_Cheatsheet.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title = Paragraph("Machine Learning Cheatsheet: Models & Techniques from Your Codebase", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 0.25*inch))

    subtitle = Paragraph("This cheatsheet is based on analysis of all Python files in your AI-ML workspace. It provides practical guidance on when to use each model/technique, with dataset-specific examples and key implementation details.", styles['Normal'])
    story.append(subtitle)
    story.append(Spacer(1, 0.25*inch))

    # Section 1: Data Preprocessing Techniques
    section_title = Paragraph("1. Data Preprocessing Techniques", styles['Heading2'])
    story.append(section_title)

    data_preprocessing = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File/Dataset"],
        ["LabelEncoder", "Convert categorical variables to numeric labels (e.g., 'Yes'/'No' to 1/0)", "from sklearn.preprocessing import LabelEncoder\nle = LabelEncoder()\ndf['column'] = le.fit_transform(df['column'])", "q13.py with Mall_Customers.csv"],
        ["MinMaxScaler", "Normalize features to [0,1] range for distance-based algorithms", "from sklearn.preprocessing import MinMaxScaler\nscaler = MinMaxScaler()\nX_scaled = scaler.fit_transform(X)", "q14.py with preprocessing.csv"],
        ["StandardScaler", "Standardize features to mean=0, std=1 for algorithms sensitive to scale", "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)", "q14.py with preprocessing.csv"],
        ["SimpleImputer", "Handle missing values with mean/median/mode", "from sklearn.impute import SimpleImputer\nimputer = SimpleImputer(strategy='mean')\nX_imputed = imputer.fit_transform(X)", "q25.py with preprocessing.csv"],
        ["train_test_split", "Split data into training/testing sets (typically 80/20)", "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)", "q20.py with preprocessing.csv"]
    ]

    table = Table(data_preprocessing)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 2: Classification Algorithms
    section_title = Paragraph("2. Classification Algorithms", styles['Heading2'])
    story.append(section_title)

    classification = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File/Dataset"],
        ["Naive Bayes (Gaussian)", "Text classification, spam detection, when features are independent", "from sklearn.naive_bayes import GaussianNB\nmodel = GaussianNB()\nmodel.fit(X_train, y_train)", "q19.py with tennis.csv\nq34.py with tennis.csv"],
        ["K-Nearest Neighbors (KNN)", "Small datasets, non-parametric classification, when decision boundary is irregular", "from sklearn.neighbors import KNeighborsClassifier\nmodel = KNeighborsClassifier(n_neighbors=5)\nmodel.fit(X_train, y_train)", "q23.py with diabetes.csv"],
        ["Decision Tree Classifier", "Interpretable models, handling categorical/mixed data, when you need feature importance", "from sklearn.tree import DecisionTreeClassifier\nmodel = DecisionTreeClassifier(max_depth=1)\nmodel.fit(X_train, y_train)", "q32.py with iris.csv\nq37.py with tennis.csv"],
        ["Support Vector Machine (SVM)", "High-dimensional data, clear margin of separation, binary/multi-class classification", "from sklearn.svm import SVC\nmodel = SVC(kernel='linear')\nmodel.fit(X_train, y_train)", "q33.py with iris.csv (uses StandardScaler)"]
    ]

    table = Table(classification)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 3: Regression Algorithms
    section_title = Paragraph("3. Regression Algorithms", styles['Heading2'])
    story.append(section_title)

    regression = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File/Dataset"],
        ["Simple Linear Regression", "Predict continuous values with one feature, linear relationship", "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)", "q35.py with salary.csv (Experience → Salary)"],
        ["Multiple Linear Regression", "Predict continuous values with multiple features", "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)", "q36.py with salary.csv (Experience, Age, Performance → Salary)"],
        ["Polynomial Regression", "Non-linear relationships, curved patterns in data", "from sklearn.preprocessing import PolynomialFeatures\nfrom sklearn.linear_model import LinearRegression\npoly = PolynomialFeatures(degree=2)\nX_poly = poly.fit_transform(X)\nmodel = LinearRegression()\nmodel.fit(X_poly, y)", "q21.py with salary.csv (Experience, Performance → Salary, degree=2)"]
    ]

    table = Table(regression)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 4: Clustering Algorithms
    section_title = Paragraph("4. Clustering Algorithms (Unsupervised)", styles['Heading2'])
    story.append(section_title)

    clustering = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File/Dataset"],
        ["K-Means Clustering", "Group similar data points, spherical clusters, when you know number of clusters", "from sklearn.cluster import KMeans\nmodel = KMeans(n_clusters=5)\nclusters = model.fit_predict(X)", "q9.py with Mall_Customers.csv"],
        ["Hierarchical Clustering", "Dendrogram visualization, no need to specify k, nested clusters", "from sklearn.cluster import AgglomerativeClustering\nmodel = AgglomerativeClustering(n_clusters=5)\nclusters = model.fit_predict(X)", "q4.py with Mall_Customers.csv"]
    ]

    table = Table(clustering)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 5: Statistical Tests
    section_title = Paragraph("5. Statistical Tests", styles['Heading2'])
    story.append(section_title)

    stats = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File/Dataset"],
        ["ANOVA (F-test)", "Compare means across 3+ groups, test if groups are significantly different", "from scipy.stats import f_oneway\nf_stat, p_value = f_oneway(group1, group2, group3)", "q30.py with preprocessing.csv"],
        ["Independent t-Test", "Compare means between 2 groups, test if two samples are different", "from scipy.stats import ttest_ind\nt_stat, p_value = ttest_ind(group1, group2)", "q31.py with preprocessing.csv"]
    ]

    table = Table(stats)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 6: Data Visualization
    section_title = Paragraph("6. Data Visualization & Analysis", styles['Heading2'])
    story.append(section_title)

    viz = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File/Dataset"],
        ["Histogram", "Understand data distribution, identify skewness/outliers", "import matplotlib.pyplot as plt\nplt.hist(data, bins=10)\nplt.show()", "q22.py with Car.csv\nq29.py with preprocessing.csv"],
        ["Box Plot", "Visualize quartiles, detect outliers", "import matplotlib.pyplot as plt\nplt.boxplot(data)\nplt.show()", "q22.py with Car.csv"],
        ["Correlation Heatmap", "Identify relationships between features", "import seaborn as sns\nsns.heatmap(df.corr(), annot=True)", "q24.py with Mall_Customers.csv"]
    ]

    table = Table(viz)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 7: Search Algorithms
    section_title = Paragraph("7. Search Algorithms", styles['Heading2'])
    story.append(section_title)

    search = [
        ["Model/Technique", "When to Use", "Key Code/Imports", "Example File"],
        ["Depth-First Search (DFS)", "Graph traversal, maze solving, when memory is limited", "Recursive implementation with visited set", "q7.py"],
        ["Breadth-First Search (BFS)", "Shortest path in unweighted graphs, level-order traversal", "Queue-based implementation", "q12.py"],
        ["Bidirectional Search", "Reduce search space, find shortest path efficiently", "Simultaneous forward/backward search", "q10.py"],
        ["Best-First Search", "Heuristic-guided search, A* algorithm foundation", "Priority queue with heuristic", "q15.py"],
        ["Depth-Limited Search (DLS)", "DFS with depth constraints to avoid infinite loops", "DFS with max_depth parameter", "q8.py"]
    ]

    table = Table(search)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Section 8: Evaluation Metrics
    section_title = Paragraph("8. Evaluation Metrics (Common for Classification)", styles['Heading2'])
    story.append(section_title)

    metrics = [
        ["Metric", "When to Use", "Key Code/Imports", "Example File"],
        ["Accuracy", "Overall correctness, balanced classes", "from sklearn.metrics import accuracy_score\naccuracy = accuracy_score(y_test, y_pred)", "q23.py"],
        ["Precision", "Minimize false positives (e.g., spam detection)", "from sklearn.metrics import precision_score\nprecision = precision_score(y_test, y_pred)", "q23.py"],
        ["Recall", "Minimize false negatives (e.g., disease detection)", "from sklearn.metrics import recall_score\nrecall = recall_score(y_test, y_pred)", "q23.py"],
        ["F1-Score", "Balance precision and recall", "from sklearn.metrics import f1_score\nf1 = f1_score(y_test, y_pred)", "q23.py"],
        ["Confusion Matrix", "Detailed classification performance breakdown", "from sklearn.metrics import confusion_matrix\ncm = confusion_matrix(y_test, y_pred)", "q23.py"],
        ["Silhouette Score", "Clustering quality, how well-separated clusters are", "from sklearn.metrics import silhouette_score\nscore = silhouette_score(X, clusters)", "q4.py"]
    ]

    table = Table(metrics)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.25*inch))

    # Quick Tips
    tips_title = Paragraph("Quick Tips from Your Codebase", styles['Heading2'])
    story.append(tips_title)

    tips = Paragraph("""
    - For polynomial regression: Always use PolynomialFeatures to transform features before fitting LinearRegression
    - Preprocessing pipeline: Missing values → Encoding → Scaling → Train-test split (see q25.py)
    - Clustering evaluation: Use Silhouette Score to determine optimal number of clusters
    - Classification metrics: Use confusion matrix for detailed analysis, F1-score for imbalanced data
    - Search algorithms: DFS for depth, BFS for breadth, Bidirectional for efficiency
    """, styles['Normal'])
    story.append(tips)

    doc.build(story)
    print(f"PDF created: {filename}")

if __name__ == "__main__":
    create_cheatsheet_pdf()
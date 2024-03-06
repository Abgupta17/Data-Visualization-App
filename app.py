# import streamlit as st
# import pandas as pd
# import os
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Set the page config and theme
# st.set_page_config(page_title='Data Visualizer', layout='centered', page_icon='📊')
# st.set_theme({'primary': '#FF5722', 'accent': '#FF9800', 'base': '#FFFFFF'})
#
# # Title
# st.title('Data Visualizer')
#
# # Specify the folder where your CSV files are located
# folder_path = r"C:\ALL IMPORTANT ML PROJ\Data Visualization App\Files"
#
# # List all files in the folder
# files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
#
# if not files:
#     st.error("No CSV files found in the specified folder.")
# else:
#     # Include a placeholder option
#     files = ['<select>'] + files
#
#     # Dropdown to select a file
#     selected_file = st.selectbox('Select a file', files)
#
#     if selected_file != '<select>':
#         # Construct the full path to the file
#         file_path = os.path.join(folder_path, selected_file)
#
#         # Read the selected CSV file
#         df = pd.read_csv(file_path)
#
#         col1, col2 = st.columns(2)
#
#         columns = df.columns.tolist()
#
#         with col1:
#             st.write("")
#             st.write(df.head())
#
#         with col2:
#             # Allow the user to select columns for plotting
#             x_axis = st.selectbox('Select the X-axis', options=columns)
#             y_axis = st.selectbox('Select the Y-axis', options=columns)
#
#             plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']
#             # Allow the user to select the type of plot
#             plot_type = st.selectbox('Select the type of plot', options=plot_list)
#
#         # Generate the plot based on user selection
#         if plot_type == 'Distribution Plot':
#             fig, ax = plt.subplots(figsize=(8, 6))
#             sns.histplot(df[x_axis], kde=True, ax=ax)
#             ax.set_xlabel(x_axis)
#             ax.set_ylabel('Density')
#             st.pyplot(fig)
#
#         elif plot_type == 'Count Plot':
#             fig, ax = plt.subplots(figsize=(8, 6))
#             sns.countplot(x=df[x_axis], ax=ax)
#             ax.set_xlabel(x_axis)
#             ax.set_ylabel('Count')
#             st.pyplot(fig)
#
#         else:
#             fig, ax = plt.subplots(figsize=(8, 6))
#             if plot_type == 'Line Plot':
#                 sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
#             elif plot_type == 'Bar Chart':
#                 sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
#             elif plot_type == 'Scatter Plot':
#                 sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
#
#             # Adjust label sizes
#             ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
#             ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size
#
#             # Adjust title and axis labels with a smaller font size
#             plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=14, fontweight='bold')
#             plt.xlabel(x_axis, fontsize=12)
#             plt.ylabel(y_axis, fontsize=12)
#
#             # Show the results
#             st.pyplot(fig)




import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config
st.set_page_config(page_title='Data Visualizer',
                   layout='wide',  # Utilize more space
                   page_icon='📊',
                   initial_sidebar_state='expanded')  # Expand sidebar by default

# Title
st.title('Data Visualizer')

# Specify the folder where your CSV files are located
folder_path = r"C:\ALL IMPORTANT ML PROJ\Data Visualization App\Files"

# List all files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

if not files:
    st.error("No CSV files found in the specified folder.")
else:
    # Include a placeholder option
    files = ['Select a file'] + files

    # Sidebar for file selection
    selected_file = st.sidebar.selectbox('Select a file', files)

    if selected_file != 'Select a file':
        # Construct the full path to the file
        file_path = os.path.join(folder_path, selected_file)

        # Read the selected CSV file
        df = pd.read_csv(file_path)

        # Display file info in sidebar
        st.sidebar.header('File Info')
        st.sidebar.markdown(f"**File Name:** {selected_file}")
        st.sidebar.markdown(f"**Total Rows:** {df.shape[0]}")
        st.sidebar.markdown(f"**Total Columns:** {df.shape[1]}")

        # Allow the user to select columns for plotting
        st.sidebar.subheader('Select Columns for Plotting')
        x_axis = st.sidebar.selectbox('X-axis', options=df.columns)
        y_axis = st.sidebar.selectbox('Y-axis', options=df.columns)

        # Allow the user to select the type of plot
        plot_type = st.sidebar.selectbox('Select Plot Type', options=['Line Plot', 'Bar Chart', 'Scatter Plot'])

        # Generate the plot based on user selection
        if st.sidebar.button('Generate Plot'):
            fig, ax = plt.subplots(figsize=(10, 6))

            if plot_type == 'Line Plot':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Bar Chart':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Scatter Plot':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)

            # Adjust label sizes
            ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
            ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size

            # Adjust title and axis labels with a smaller font size
            plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=16, fontweight='bold')
            plt.xlabel(x_axis, fontsize=12)
            plt.ylabel(y_axis, fontsize=12)

            # Show the plot
            st.pyplot(fig)

        # Display dataframe
        st.header('Preview of Data')
        st.write(df.head(10))  # Display first 10 rows of the dataframe

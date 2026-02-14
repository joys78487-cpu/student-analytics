import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os

from django.shortcuts import render
from .models import StudentRecord
from .forms import UploadFileForm


# ==============================
# Upload View
# ==============================

def upload_file(request):
    message = ""

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name
            extension = os.path.splitext(file_name)[1].lower()

            try:
                # -------- File Type Support --------
                if extension == '.csv':
                    df = pd.read_csv(uploaded_file)

                elif extension in ['.xlsx', '.xls']:
                    df = pd.read_excel(uploaded_file)

                elif extension == '.json':
                    df = pd.read_json(uploaded_file)

                else:
                    message = "Unsupported file format! Upload CSV, Excel or JSON."
                    return render(request, 'analytics/upload.html', {
                        'form': form,
                        'message': message
                    })

                # -------- Clear Old Data --------
                StudentRecord.objects.all().delete()

                # -------- Insert Data --------
                for _, row in df.iterrows():
                    StudentRecord.objects.create(
                        name=row['Name'],
                        maths=row['Maths'],
                        science=row['Science'],
                        english=row['English'],
                        computer=row['Computer']
                    )

                message = "File uploaded successfully!"

            except Exception as e:
                message = f"Error: {str(e)}"

    else:
        form = UploadFileForm()

    return render(request, 'analytics/upload.html', {
        'form': form,
        'message': message
    })


# ==============================
# Dashboard View
# ==============================

def dashboard(request):
    students = StudentRecord.objects.all()

    if not students.exists():
        return render(request, 'analytics/dashboard.html', {
            'message': "No data available. Please upload a file."
        })

    # Convert QuerySet to DataFrame
    df = pd.DataFrame(list(students.values()))

    # -------- Subject Averages --------
    subject_avg = df[['maths', 'science', 'english', 'computer']].mean()

    # -------- Total & Rank --------
    df['total'] = df[['maths', 'science', 'english', 'computer']].sum(axis=1)
    df['rank'] = df['total'].rank(ascending=False, method='min').astype(int)

    # -------- Topper --------
    topper = df.loc[df['total'].idxmax()]['name']

    # -------- Fail Percentage --------
    fail_count = (
        df[['maths', 'science', 'english', 'computer']] < 40
    ).any(axis=1).sum()

    total_students = len(df)
    fail_percent = round((fail_count / total_students) * 100, 2)

    # -------- Graph Generation (FIXED) --------
    fig, ax = plt.subplots(figsize=(7, 5))
    subject_avg.plot(kind='bar', ax=ax)

    ax.set_title("Subject Averages")
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Average Marks")

    plt.xticks(rotation=45)
    plt.tight_layout() 

    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')

    buffer.close()
    plt.close(fig)

    # -------- Context --------
    context = {
        'graph': graph,
        'total_students': total_students,
        'topper': topper,
        'fail_percent': fail_percent,
        'students': df.to_dict('records')
    }

    return render(request, 'analytics/dashboard.html', context)

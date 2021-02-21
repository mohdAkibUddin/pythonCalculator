import csv


class CSVReader:
    rows = []

    def readCSV(self, filepath):
        csvFile = open(filepath)
        csvReader = csv.DictReader(csvFile, delimeter=',')
        for row in csvReader:
            self.rows.append(row)
        csvFile.close()
        return self.rows

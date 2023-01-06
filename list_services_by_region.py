import boto3
import csv

session = boto3.Session()

all_services = session.get_available_services()
all_regions = session.get_available_regions(service_name='ec2')

services = [service for service in all_services]
regions = [region for region in all_regions]

with open('services.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    header_row = ['Services'] + regions
    writer.writerow(header_row)

    for service in services:
        
        availability = session.get_available_regions(service)

        if availability:
            service_availability_row = []
            
            for region in all_regions:
                if region in availability :
                    service_availability_row.append("X")
                else:
                    service_availability_row.append("")

            row = [service] + service_availability_row
            writer.writerow(row)

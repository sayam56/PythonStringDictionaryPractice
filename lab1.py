def main():
    total_rainfall = 0.0

    monthly_rainfall = [0.0] * 12
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(12):
        monthly_rainfall[i] = float(input('Enter the rainfall for '+ months[i] + ': '))
        total_rainfall += monthly_rainfall[i]

    # avg monthly rainfall
    average_rainfall = total_rainfall / 12

    # highest and lowest rainfall
    max_rainfall = max(monthly_rainfall)
    min_rainfall = min(monthly_rainfall)
    max_month = months[monthly_rainfall.index(max_rainfall)]
    min_month = months[monthly_rainfall.index(min_rainfall)]

    # Display output
    print('Total rainfall for the year:', total_rainfall)
    print('Average monthly rainfall:', average_rainfall)
    print('Month with the highest rainfall:', max_month)
    print('Month with the lowest rainfall:', min_month)

# Call the main function.
if __name__ == '__main__':
    main()

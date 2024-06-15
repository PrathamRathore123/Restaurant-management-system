
import json

def get_rating(reviews):
    if reviews:
        rating = sum(reviews) // len(reviews)
    else:
        rating = 0
    return '★'*rating

def main():
    try:
        with open('main.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'items': []}

    items = data.get('items', [])

    while True:
        print('-'*40)
        print('<<<<<Parth,s...Restaurant>>>>>')
        print('-'*40)
        print('1. Show Menu')
        print('2. Order Items')
        print('3. Update Menu')
        print('4. Add Rating')
        print('5. Exit')
        print('-'*40)
        choice = int(input('Enter your choice: '))

        if choice == 1:
            print('-'*40)
            print('ID\tName\t\tPrice\tRating')
            print('-'*40)
            for item in items:
                print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}\t{get_rating(item.get("reviews", []))}')
            print('-'*40)
        elif choice == 2:
            ordered_items = {}
            order_items = list(map(int, input('What items do you want to try today? (comma separated IDs): ').split(',')))
            print('-'*40)
            print('ID\tName\t\tPrice\tQuantity\tAmount')
            print('-'*40)
            total_bill = 0
            for order_item in order_items:
                for item in items:
                    if item['id'] == order_item:
                        if order_item in ordered_items:
                            ordered_items[order_item]['quantity'] += 1
                        else:
                            ordered_items[order_item] = item
                            ordered_items[order_item]['quantity'] = 1
                        break

            for item_id, item in ordered_items.items():
                name = item['name']
                price = item['price']
                quantity = item['quantity']
                amount = price * quantity
                print(f'{item_id}\t{name}\t{price}\t{quantity}\t\t{amount}')
                total_bill += amount
            
            print(f'\t Total Amount: {total_bill}')
            print('-'*40)     
        elif choice == 3:
            name = input('Enter item name: ')
            item_price = int(input('Enter the price: '))
            item_type = input('veg or non-veg: ')
            items.append({
                'id': len(items) + 1,
                'name': name,
                'price': item_price,
                'veg': True if item_type == 'veg' else False,
                'reviews': []
            })

            data['items'] = items
            with open('main.json', 'w') as f:
                json.dump(data, f, indent=4)
            print('Item is added.')
        elif choice == 4:
            item_id = int(input('Enter the item id: '))
            rating = int(input('Give your rating 1-5: '))
            for item in items:
                if item['id'] == item_id:
                    item['reviews'].append(rating)
                    break
            data['items'] = items
            with open('main.json', 'w') as f:
                json.dump(data, f, indent=4)
            print('Thank you. Your Rating is recorded.')
        else:
            print('Thank You')
            break

if __name__ == "__main__":
    main()
require 'sinatra'
require 'sinatra/reloader'

class Store
	@username
	@address
	@phone
	@product
	@price
	@quantity
	@@price_sum

	def initialize(username,address,phone,product,price,quantity)
		@username = username
		@address = address
		@phone = phone
		@product = product
		@price = price
		@quantity = quantity
	end

	def self.price_sum
		@@price_sum
	end

	def price_calculate()
		@@price_sum = 0
		if @product != nil
			for i in (0...@product.length)
				@@price_sum += @price[i].to_i * @quantity[i].to_i
			end
		end
		return @@price_sum
	end
end

get '/' do
	username = params['username']
	address = params['address']
	phone = params['phone']
	product = params['productname']
	price = params['price']
	quantity = params['quantity']
	if product != nil
		product = product.split(', ')
		price = price.split(', ')
		quantity = quantity.split(', ')
	end
	single_product = Store.new(username,address,phone,product,price,quantity)
	single_product.price_calculate()
	erb :index, :locals => {:price_sum => Store.price_sum,:username => username,:address => address,:phone => phone,:product => product,:price => price,:quantity => quantity}
end
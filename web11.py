import React, { useState, useEffect } from 'react';
import { ShoppingCart, ArrowLeft, CheckCircle, Package, Home, Info } from 'lucide-react';

// --- MOCK DATA ---
// In a real application, this would come from a database.
const products = [
  {
    id: 1,
    name: 'Ultimate UI Kit',
    price: 49.99,
    description: 'A comprehensive UI kit with over 500 components, perfect for designing modern web and mobile applications. Includes Figma and Sketch files.',
    imageUrl: 'https://placehold.co/600x400/1e40af/ffffff?text=UI+Kit',
    digitalFile: 'ultimate_ui_kit_v1.zip',
  },
  {
    id: 2,
    name: 'Ebook: Mastering React',
    price: 29.99,
    description: 'Learn React from scratch with this 200-page ebook. Covers hooks, state management, and best practices for building scalable applications.',
    imageUrl: 'https://placehold.co/600x400/be185d/ffffff?text=React+Ebook',
    digitalFile: 'mastering_react_ebook.pdf',
  },
  {
    id: 3,
    name: 'Photography Preset Pack',
    price: 19.99,
    description: 'A collection of 20 professional Lightroom presets to give your photos a stunning, cinematic look. Compatible with desktop and mobile.',
    imageUrl: 'https://placehold.co/600x400/9a3412/ffffff?text=Presets',
    digitalFile: 'photo_preset_pack.zip',
  },
  {
    id: 4,
    name: 'Minimalist Icon Set',
    price: 15.00,
    description: 'Over 1000 minimalist vector icons for your projects. Provided in SVG, and PNG formats for easy use.',
    imageUrl: 'https://placehold.co/600x400/4d7c0f/ffffff?text=Icon+Set',
    digitalFile: 'minimalist_icons.svg',
  },
];

// --- COMPONENTS ---

const Header = ({ navigateTo, cartItemCount }) => (
  <header className="bg-white/80 backdrop-blur-md shadow-sm sticky top-0 z-40">
    <div className="container mx-auto px-6 py-4 flex justify-between items-center">
      <div className="text-2xl font-bold text-gray-800 cursor-pointer" onClick={() => navigateTo('home')}>
        <span className="text-indigo-600">Digi</span>Sell
      </div>
      <nav className="hidden md:flex items-center space-x-8">
        <a href="#" onClick={(e) => { e.preventDefault(); navigateTo('home'); }} className="text-gray-600 hover:text-indigo-600 transition-colors">Home</a>
        <a href="#" onClick={(e) => { e.preventDefault(); navigateTo('products'); }} className="text-gray-600 hover:text-indigo-600 transition-colors">Products</a>
        <a href="#" onClick={(e) => { e.preventDefault(); navigateTo('about'); }} className="text-gray-600 hover:text-indigo-600 transition-colors">About</a>
      </nav>
      <div className="relative cursor-pointer" onClick={() => navigateTo('checkout')}>
        <ShoppingCart className="h-6 w-6 text-gray-600 hover:text-indigo-600 transition-colors" />
        {cartItemCount > 0 && (
          <span className="absolute -top-2 -right-2 bg-indigo-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
            {cartItemCount}
          </span>
        )}
      </div>
    </div>
  </header>
);

const Footer = () => (
    <footer className="bg-gray-100 text-gray-600">
        <div className="container mx-auto px-6 py-8">
            <div className="flex flex-col md:flex-row justify-between items-center">
                <div className="text-lg font-bold text-gray-800 mb-4 md:mb-0">
                    <span className="text-indigo-600">Digi</span>Sell
                </div>
                <div className="flex space-x-6 mb-4 md:mb-0">
                    <a href="#" className="hover:text-indigo-600">Privacy Policy</a>
                    <a href="#" className="hover:text-indigo-600">Terms of Service</a>
                    <a href="#" className="hover:text-indigo-600">Contact</a>
                </div>
                <p className="text-sm">&copy; {new Date().getFullYear()} DigiSell. All rights reserved.</p>
            </div>
        </div>
    </footer>
);


const HomePage = ({ navigateTo }) => (
  <div className="flex-grow">
    {/* Hero Section */}
    <section className="bg-indigo-50 text-center py-20 md:py-32">
      <div className="container mx-auto px-6">
        <h1 className="text-4xl md:text-6xl font-extrabold text-gray-800 mb-4">Your One-Stop Digital Marketplace</h1>
        <p className="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto mb-8">
          Discover high-quality digital products, from UI kits to ebooks, to accelerate your creative workflow.
        </p>
        <button
          onClick={() => navigateTo('products')}
          className="bg-indigo-600 text-white font-bold py-3 px-8 rounded-lg shadow-lg hover:bg-indigo-700 transition-transform transform hover:scale-105"
        >
          Browse Products
        </button>
      </div>
    </section>

    {/* Featured Products */}
    <section className="py-16">
        <div className="container mx-auto px-6">
            <h2 className="text-3xl font-bold text-center text-gray-800 mb-10">Featured Products</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {products.slice(0, 3).map(product => (
                    <ProductCard key={product.id} product={product} navigateTo={navigateTo} />
                ))}
            </div>
        </div>
    </section>
  </div>
);

const ProductCard = ({ product, navigateTo }) => (
    <div className="bg-white rounded-lg shadow-md overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 cursor-pointer" onClick={() => navigateTo('productDetail', product)}>
        <img src={product.imageUrl} alt={product.name} className="w-full h-56 object-cover" onError={(e) => { e.target.onerror = null; e.target.src = 'https://placehold.co/600x400/cccccc/ffffff?text=Image+Not+Found'; }}/>
        <div className="p-6">
            <h3 className="text-xl font-semibold text-gray-800 mb-2">{product.name}</h3>
            <p className="text-2xl font-bold text-indigo-600">${product.price}</p>
        </div>
    </div>
);

const ProductsPage = ({ navigateTo }) => (
  <div className="flex-grow container mx-auto px-6 py-12">
    <h1 className="text-4xl font-bold text-center text-gray-800 mb-12">All Products</h1>
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      {products.map(product => (
        <ProductCard key={product.id} product={product} navigateTo={navigateTo} />
      ))}
    </div>
  </div>
);

const ProductDetailPage = ({ product, navigateTo, addToCart }) => (
  <div className="flex-grow container mx-auto px-6 py-12">
    <button onClick={() => navigateTo('products')} className="flex items-center text-gray-600 hover:text-indigo-600 mb-8">
      <ArrowLeft className="h-5 w-5 mr-2" />
      Back to Products
    </button>
    <div className="flex flex-col lg:flex-row gap-12">
      <div className="lg:w-1/2">
        <img src={product.imageUrl} alt={product.name} className="w-full rounded-lg shadow-lg" onError={(e) => { e.target.onerror = null; e.target.src = 'https://placehold.co/600x400/cccccc/ffffff?text=Image+Not+Found'; }}/>
      </div>
      <div className="lg:w-1/2">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">{product.name}</h1>
        <p className="text-4xl font-bold text-indigo-600 mb-6">${product.price}</p>
        <p className="text-gray-600 leading-relaxed mb-8">{product.description}</p>
        <button
          onClick={() => {
            addToCart(product);
            navigateTo('checkout');
          }}
          className="w-full bg-indigo-600 text-white font-bold py-4 px-8 rounded-lg shadow-lg hover:bg-indigo-700 transition-all flex items-center justify-center space-x-2"
        >
          <ShoppingCart className="h-6 w-6" />
          <span>Add to Cart & Checkout</span>
        </button>
      </div>
    </div>
  </div>
);

const AboutPage = () => (
    <div className="flex-grow container mx-auto px-6 py-16">
        <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-4xl md:text-5xl font-bold text-gray-800 mb-6">About <span className="text-indigo-600">Digi</span>Sell</h1>
            <p className="text-lg text-gray-600 mb-8 leading-relaxed">
                DigiSell was founded with a simple mission: to provide creators, developers, and designers with high-quality digital assets that are both affordable and easy to use. We believe that great tools empower great work, and we're passionate about curating a collection of products that help you bring your ideas to life faster.
            </p>
            <div className="bg-white p-8 rounded-lg shadow-md border border-gray-200">
                <h2 className="text-2xl font-semibold text-gray-800 mb-4">Our Philosophy</h2>
                <p className="text-gray-600">
                    We focus on quality over quantity. Every product on our platform is carefully reviewed to ensure it meets our high standards for design, functionality, and documentation. When you purchase from DigiSell, you're not just getting a file; you're getting a tool that has been thoughtfully crafted to be a joy to use.
                </p>
            </div>
        </div>
    </div>
);


const CheckoutPage = ({ cart, removeFromCart, navigateTo, clearCart }) => {
  const [customerEmail, setCustomerEmail] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const total = cart.reduce((sum, item) => sum + item.price, 0);

  const handlePayment = (e) => {
    e.preventDefault();
    if (!customerEmail || cart.length === 0) {
      alert('Please provide your email and add items to your cart.');
      return;
    }
    
    setIsProcessing(true);
    
    // --- SIMULATION ---
    // In a real app, you would integrate with Stripe/PayPal here.
    // This timeout simulates the network request to the payment gateway.
    setTimeout(() => {
      console.log('Payment successful for:', customerEmail);
      console.log('Sending files for products:', cart.map(p => p.digitalFile));
      
      // This is where you would trigger a backend process
      // to send the actual emails with download links.
      
      setIsProcessing(false);
      navigateTo('confirmation', { email: customerEmail, items: cart });
      clearCart();
    }, 2000);
  };

  if (cart.length === 0) {
    return (
      <div className="flex-grow container mx-auto px-6 py-12 text-center">
        <ShoppingCart className="h-24 w-24 mx-auto text-gray-300" />
        <h1 className="text-3xl font-bold text-gray-800 mt-6 mb-2">Your Cart is Empty</h1>
        <p className="text-gray-600 mb-6">Looks like you haven't added any products yet.</p>
        <button
          onClick={() => navigateTo('products')}
          className="bg-indigo-600 text-white font-bold py-3 px-6 rounded-lg shadow-md hover:bg-indigo-700 transition-colors"
        >
          Explore Products
        </button>
      </div>
    );
  }

  return (
    <div className="flex-grow bg-gray-50">
      <div className="container mx-auto px-6 py-12">
        <h1 className="text-4xl font-bold text-center text-gray-800 mb-12">Checkout</h1>
        <div className="flex flex-col lg:flex-row gap-12">
          {/* Order Summary */}
          <div className="lg:w-1/2 bg-white p-8 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold text-gray-800 border-b pb-4 mb-6">Order Summary</h2>
            {cart.map(item => (
              <div key={item.id} className="flex justify-between items-center mb-4">
                <div>
                  <p className="font-semibold text-gray-700">{item.name}</p>
                  <button onClick={() => removeFromCart(item.id)} className="text-sm text-red-500 hover:text-red-700">Remove</button>
                </div>
                <p className="font-semibold text-gray-800">${item.price.toFixed(2)}</p>
              </div>
            ))}
            <div className="border-t mt-6 pt-4 flex justify-between items-center font-bold text-xl">
              <p>Total</p>
              <p>${total.toFixed(2)}</p>
            </div>
          </div>

          {/* Payment Form */}
          <div className="lg:w-1/2 bg-white p-8 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold text-gray-800 border-b pb-4 mb-6">Payment Information</h2>
            <form onSubmit={handlePayment}>
              <div className="mb-4">
                <label htmlFor="email" className="block text-gray-700 font-semibold mb-2">Email Address</label>
                <p className="text-sm text-gray-500 mb-2">Your digital products will be sent to this email.</p>
                <input
                  type="email"
                  id="email"
                  value={customerEmail}
                  onChange={(e) => setCustomerEmail(e.target.value)}
                  className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  placeholder="you@example.com"
                  required
                />
              </div>
              
              {/* Mock Payment Fields */}
              <div className="mb-4">
                <label htmlFor="card" className="block text-gray-700 font-semibold mb-2">Card Information (Mock)</label>
                <div className="bg-gray-100 p-4 rounded-lg border">
                    <p className="text-gray-600">This is a simulated payment form.</p>
                    <p className="text-sm text-gray-500">No real card details are needed.</p>
                </div>
              </div>

              <button
                type="submit"
                disabled={isProcessing}
                className="w-full bg-indigo-600 text-white font-bold py-4 px-8 rounded-lg shadow-lg hover:bg-indigo-700 transition-all disabled:bg-indigo-300 disabled:cursor-not-allowed flex items-center justify-center"
              >
                {isProcessing ? (
                  <>
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Processing Payment...
                  </>
                ) : `Pay $${total.toFixed(2)}`}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

const ConfirmationPage = ({ data, navigateTo }) => {
  const { email, items } = data;
  return (
    <div className="flex-grow container mx-auto px-6 py-16 flex flex-col items-center justify-center text-center">
      <CheckCircle className="h-24 w-24 text-green-500 mb-6" />
      <h1 className="text-4xl font-bold text-gray-800 mb-4">Payment Successful!</h1>
      <p className="text-lg text-gray-600 max-w-2xl mb-8">
        Thank you for your purchase. A confirmation email with download links for your products has been sent to <strong className="text-indigo-600">{email}</strong>.
      </p>
      
      <div className="bg-white p-6 rounded-lg shadow-md border w-full max-w-lg mb-8">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">Products Purchased:</h2>
        <ul className="text-left">
          {items.map(item => (
            <li key={item.id} className="flex items-center justify-between py-2 border-b">
                <span className="flex items-center"><Package className="h-5 w-5 mr-3 text-indigo-500"/>{item.name}</span>
                <span className="font-mono text-gray-600">${item.price.toFixed(2)}</span>
            </li>
          ))}
        </ul>
      </div>

      <button
        onClick={() => navigateTo('home')}
        className="bg-indigo-600 text-white font-bold py-3 px-8 rounded-lg shadow-md hover:bg-indigo-700 transition-colors flex items-center"
      >
        <Home className="h-5 w-5 mr-2" />
        Return to Home
      </button>
    </div>
  );
};


// --- MAIN APP COMPONENT ---
export default function App() {
  const [page, setPage] = useState('home');
  const [pageData, setPageData] = useState(null);
  const [cart, setCart] = useState([]);

  const navigateTo = (newPage, data = null) => {
    setPage(newPage);
    setPageData(data);
    window.scrollTo(0, 0);
  };

  const addToCart = (product) => {
    // Prevent adding the same item multiple times
    if (!cart.find(item => item.id === product.id)) {
      setCart(prevCart => [...prevCart, product]);
    }
  };

  const removeFromCart = (productId) => {
    setCart(prevCart => prevCart.filter(item => item.id !== productId));
  };
  
  const clearCart = () => {
      setCart([]);
  };

  const renderPage = () => {
    switch (page) {
      case 'home':
        return <HomePage navigateTo={navigateTo} />;
      case 'products':
        return <ProductsPage navigateTo={navigateTo} />;
      case 'productDetail':
        return <ProductDetailPage product={pageData} navigateTo={navigateTo} addToCart={addToCart} />;
      case 'about':
        return <AboutPage />;
      case 'checkout':
        return <CheckoutPage cart={cart} removeFromCart={removeFromCart} navigateTo={navigateTo} clearCart={clearCart}/>;
      case 'confirmation':
        return <ConfirmationPage data={pageData} navigateTo={navigateTo} />;
      default:
        return <HomePage navigateTo={navigateTo} />;
    }
  };

  return (
    <div className="bg-gray-50 min-h-screen flex flex-col font-sans">
      <Header navigateTo={navigateTo} cartItemCount={cart.length} />
      <main className="flex-grow">
        {renderPage()}
      </main>
      <Footer />
    </div>
  );
}

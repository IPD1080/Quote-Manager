# File: catalog.py

product_catalog = {
    "Independent Print": {
        "Business Cards": {
            "inputs": ["Quantity", "Sides", "Paper Type", "Finish"],
            "price_per_100": 12.00
        },
        "Flyers": {
            "inputs": ["Quantity", "Size", "Paper Type", "Coating", "Sides"],
            "price_per_100": 15.00
        },
        "Brochures": {
            "inputs": ["Quantity", "Size", "Paper Type", "Fold Type", "Coating"],
            "price_per_100": 20.00
        },
        "Postcards": {
            "inputs": ["Quantity", "Size", "Paper Type", "Coating", "Sides"],
            "price_per_100": 14.00
        },
        "Booklets": {
            "inputs": ["Quantity", "Size", "Paper Type", "Binding"],
            "price_per_100": 40.00
        },
        "Posters": {
            "inputs": ["Quantity", "Size", "Paper Type", "Finish"],
            "price_per_100": 25.00
        },
        "Stickers": {
            "inputs": ["Quantity", "Size", "Shape", "Finish"],
            "price_per_100": 18.00
        },
        "Banners": {
            "inputs": ["Size", "Grommets", "Hemming"],
            "pricing": {
                "2x4": 30.00,
                "3x6": 45.00,
                "4x8": 60.00
            }
        },
        "Yard Signs": {
            "inputs": ["Quantity", "Size", "Sides"],
            "price_per_100": 60.00
        },
        "Canvas Prints": {
            "inputs": ["Quantity", "Size"],
            "pricing": {
                "12x12": 35.00,
                "16x20": 45.00,
                "12x18": 40.00,
                "36x48": 80.00
            }
        },
        "Window Clings": {
            "inputs": ["Quantity", "Size"],
            "pricing": {
                "18x24": 20.00,
                "24x36": 30.00
            }
        },
        "Wall Decals": {
            "inputs": ["Size", "Shape", "Material"],
            "pricing": {
                "24x36": 28.00,
                "36x48": 40.00
            }
        },
        "Apparel": {
            "inputs": ["Quantity", "Print Area", "Number of Colors"],
            "base_price_per_unit": 9.00,
            "extra_color_cost": 1.50,
            "back_print_cost": 4.00
        }
    },
    "Independent Wraps": {
        "Spot Graphics": {
            "inputs": ["Graphic Count", "Material"],
            "price_per_graphic": 75.00
        },
        "Vehicle Lettering": {
            "inputs": ["Text Length", "Font Type", "Color"],
            "base_price": 250.00
        },
        "Window Decals": {
            "inputs": ["Size", "Laminate?"],
            "pricing": {
                "18x24": 55.00,
                "24x36": 75.00
            }
        },
        "Fleet Graphics": {
            "inputs": ["Vehicle Count", "Complexity"],
            "base_price_per_vehicle": 900.00
        },
        "Color Change Wrap": {
            "inputs": ["Vehicle Type", "Finish"],
            "pricing": {
                "Sedan": 2200.00,
                "SUV": 2600.00,
                "Truck": 2800.00
            }
        },
        "Chrome Delete": {
            "inputs": ["Parts"],
            "price_per_part": 50.00
        },
        "Partial Wrap": {
            "inputs": ["Sq Ft", "Include Laminate"],
            "base_price_per_sqft": 18.00
        },
        "Roof Wrap": {
            "inputs": ["Size"],
            "pricing": {
                "4x4": 180.00,
                "5x5": 225.00
            }
        },
        "Hood Wrap": {
            "inputs": ["Size"],
            "pricing": {
                "4x4": 160.00,
                "5x5": 200.00
            }
        },
        "Racing Stripes": {
            "inputs": ["Length", "Color"],
            "price_per_foot": 18.00
        },
        "Carbon Fiber Accents": {
            "inputs": ["Item Type"],
            "base_price": 125.00
        },
        "Paint Protection Film": {
            "inputs": ["Panel Count"],
            "price_per_panel": 95.00
        },
        "Reflective Wrap": {
            "inputs": ["Sq Ft"],
            "price_per_sqft": 25.00
        },
        "Finish Options": {
            "inputs": ["Finish"],
            "pricing": {
                "Gloss": 0.00,
                "Matte": 150.00,
                "Satin": 150.00,
                "Color Flip": 300.00
            }
        }
    }
}

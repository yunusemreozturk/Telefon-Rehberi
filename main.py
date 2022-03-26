class Menu:
    def userAdd(self):
        self.users = {}

        name = input("İsim: ").lower().strip()
        surname = input("Soyisim: ").lower().strip()
        phoneNumber = input("Telefon Numarası: ").strip()

        while phoneNumber.len() == 11:
            phoneNumber = input("Telefon Numarası: ")

        confirmation = input(f"İsim: {name} Telefon Numarası: {phoneNumber}\nOnaylıyor musun?(e/h)")

        if confirmation == 'e':
            self.users["Name"] = [name + " " + surname]
            self.users["Phone Number"] = phoneNumber
        elif confirmation == 'h':
            pass  # hayır diyince ana ekrana atsın
        else:
            print("Sadece E veya H yazılabilir.")

    def delUser(self):
        delete = input("Silmek istediğiniz kullanıcı ismi? ").lower().strip()

        if delete in self.users:
            confirmation = input(
                f"Adı: {delete} Telefon Numarası: {self.users[delete]} \nSilmek istediğinize emin misiniz?(e/h)")

            if confirmation == 'e':
                del self.users[delete]

                print(f"{delete} silindi.")
            elif confirmation == 'h':
                pass  # hayır diyince ana ekrana atsın
            else:
                print("Sadece E veya H yazılabilir.")

    def searchUser(self):
        search = input("1- İsim\n2- Telefon Numarası")
        if search == 1:
            searchUser = input("İsim: ")
            self.users.get(searchUser, "")
        elif search == 2:
            pass
        else:
            print("Sadece 1 veya 2 yazılabilir.")

class Users:
    pass

# dictionaryde name kısmına ulaşmada kaldın
